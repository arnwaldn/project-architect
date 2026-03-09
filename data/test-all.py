#!/usr/bin/env python3
"""Full integration test suite for project-architect plugin."""
import sys, os, json, re

sys.stdout.reconfigure(encoding="utf-8")
os.chdir(r"C:\Users\arnau\Documents\projets\skill project-architect")

errors = []
warnings = []
passed = 0

# T1: Plugin structure
required = [
    ".claude-plugin/plugin.json", "commands/project-architect.md",
    "agents/discovery-auditor.md", "agents/spec-architect.md",
    "agents/tech-architect.md", "agents/pre-dev-validator.md",
    "templates/brief-projet.md", "templates/cahier-des-charges.md",
    "templates/architecture-doc.md", "templates/planning-projet.md",
    "templates/checklist-pre-dev.md", "templates/CLAUDE-project.md",
    "templates/implementation-roadmap.md", "data/adaptation-matrix.json",
]
missing = [p for p in required if not os.path.exists(p)]
if not missing:
    passed += 1
    print("[PASS] T1: Structure - 14/14 files present")
else:
    errors.append("Missing: %s" % missing)
    print("[FAIL] T1: Missing files: %s" % missing)

# T2: plugin.json
with open(".claude-plugin/plugin.json", "r", encoding="utf-8") as f:
    plugin = json.load(f)
if all(k in plugin for k in ["name", "version", "description", "agents", "skills"]):
    passed += 1
    print("[PASS] T2: plugin.json valid (name=%s, v=%s, %d agents)" % (
        plugin["name"], plugin["version"], len(plugin["agents"])))
else:
    errors.append("plugin.json missing fields")
    print("[FAIL] T2: plugin.json incomplete")

# T3: Matrix JSON
with open("data/adaptation-matrix.json", "r", encoding="utf-8") as f:
    matrix = json.load(f)
exp_phases = ["qualifier", "comprendre", "strategiser", "specifier",
              "designer", "architecturer", "planifier", "valider"]
phases_ok = all(p in matrix["phases"] for p in exp_phases)
order_ok = matrix["phase_order"] == exp_phases
monotonic = True
for p in exp_phases:
    counts = [len(matrix["phases"][p]["items"][s]) for s in ["S", "M", "L", "XL"]]
    if counts != sorted(counts):
        monotonic = False
total = sum(len(matrix["phases"][p]["items"][s]) for p in exp_phases for s in ["S", "M", "L", "XL"])
if phases_ok and order_ok and monotonic:
    passed += 1
    print("[PASS] T3: Matrix valid (8 phases, monotonic, %d total items)" % total)
else:
    errors.append("Matrix issues (phases=%s, order=%s, mono=%s)" % (phases_ok, order_ok, monotonic))
    print("[FAIL] T3: Matrix problems")

# T4: Skill file structure
with open("commands/project-architect.md", "r", encoding="utf-8") as f:
    skill = f.read()
lines_count = skill.count("\n") + 1
phase_markers = ["## Phase %d :" % i for i in range(1, 9)]
positions = [skill.find(m) for m in phase_markers]
all_found = all(p != -1 for p in positions)
in_order = positions == sorted(positions)
no_dups = all(skill.count(m) == 1 for m in phase_markers)
if all_found and in_order and no_dups:
    passed += 1
    print("[PASS] T4: Skill structure (%d lines, 8 phases in order, no duplicates)" % lines_count)
else:
    errors.append("Skill structure issue (found=%s, order=%s, dups=%s)" % (all_found, in_order, no_dups))
    print("[FAIL] T4: Skill structure problems")

# T5: Question numbering
questions = re.findall(r"\*\*Q(\d+)\.(\d+)\*\*", skill)
by_phase = {}
for pn, qn in questions:
    by_phase.setdefault(int(pn), []).append(int(qn))
all_continuous = True
for pn in sorted(by_phase):
    nums = sorted(by_phase[pn])
    expected = list(range(1, max(nums) + 1))
    if nums != expected:
        all_continuous = False
        warnings.append("Phase %d: expected %s, got %s" % (pn, expected, nums))
if all_continuous:
    passed += 1
    print("[PASS] T5: Question numbering (%d questions across 8 phases, all continuous)" % len(questions))
else:
    errors.append("Question numbering gaps")
    print("[FAIL] T5: Question numbering issues")
    for w in warnings:
        print("  " + w)

# T6: Phase 5 enrichment
p5s = skill.find("## Phase 5 : DESIGNER")
p6s = skill.find("## Phase 6 : ARCHITECTURER")
phase5 = skill[p5s:p6s]
blocs = len(re.findall(r"\*\*Bloc \d+", phase5))
q5s_count = len(re.findall(r"\*\*Q5\.\d+\*\*", phase5))
has_2parts = "Partie 1" in phase5 and "Partie 2" in phase5
has_ckpt = "Checkpoint" in phase5
if blocs == 9 and q5s_count == 24 and has_2parts and has_ckpt:
    passed += 1
    print("[PASS] T6: Phase 5 enriched (9 blocs, 24 questions, 2-part livrable, checkpoint)")
else:
    errors.append("Phase 5: blocs=%d q=%d 2parts=%s ckpt=%s" % (blocs, q5s_count, has_2parts, has_ckpt))
    print("[FAIL] T6: Phase 5 issues")

# T7: V2 bridge in Phase 8
p8s = skill.find("## Phase 8 : VALIDER")
phase8 = skill[p8s:]
bridge_kw = ["CLAUDE.md", "implementation-roadmap.md", "docs/preparation", "fichiers-pont", "CLAUDE-project.md"]
missing_kw = [kw for kw in bridge_kw if kw not in phase8]
if not missing_kw:
    passed += 1
    print("[PASS] T7: V2 bridge generation (all 5 keywords in Phase 8)")
else:
    errors.append("Bridge missing: %s" % missing_kw)
    print("[FAIL] T7: Bridge missing: %s" % missing_kw)

# T8: Templates
tpl_dir = "templates"
tpl_files = [f for f in os.listdir(tpl_dir) if f.endswith(".md")]
brace_issues = []
for tf in tpl_files:
    with open(os.path.join(tpl_dir, tf), "r", encoding="utf-8") as f:
        tc = f.read()
    if tc.count("{") != tc.count("}"):
        brace_issues.append(tf)
if not brace_issues:
    passed += 1
    print("[PASS] T8: Templates (%d files, all braces balanced)" % len(tpl_files))
else:
    errors.append("Brace issues in: %s" % brace_issues)
    print("[FAIL] T8: Template brace issues in %s" % brace_issues)

# T9: Plugin installation
ip_path = os.path.expanduser("~/.claude/plugins/installed_plugins.json")
settings_path = os.path.expanduser("~/.claude/settings.json")
with open(ip_path, "r", encoding="utf-8") as f:
    ip = json.load(f)
with open(settings_path, "r", encoding="utf-8") as f:
    settings = json.load(f)
plugins_data = ip.get("plugins", ip)
installed = "project-architect@local" in plugins_data
enabled = settings.get("enabledPlugins", {}).get("project-architect@local") is True
if installed and enabled:
    passed += 1
    print("[PASS] T9: Plugin installed and enabled")
else:
    errors.append("installed=%s enabled=%s" % (installed, enabled))
    print("[FAIL] T9: Plugin config issue")

# T10: Cache sync
cache_base = os.path.expanduser("~/.claude/plugins/cache/local/project-architect/1.0.0")
key_files = [
    "commands/project-architect.md", "data/adaptation-matrix.json",
    "templates/CLAUDE-project.md", "templates/implementation-roadmap.md",
]
cache_ok = True
for kf in key_files:
    src_size = os.path.getsize(kf)
    cp = os.path.join(cache_base, kf.replace("/", os.sep))
    if os.path.exists(cp):
        cs = os.path.getsize(cp)
        if src_size != cs:
            cache_ok = False
            errors.append("%s: src=%d cache=%d" % (kf, src_size, cs))
    else:
        cache_ok = False
        errors.append("%s: not in cache" % kf)

orphaned = os.path.join(cache_base, ".orphaned_at")
if os.path.exists(orphaned):
    cache_ok = False
    errors.append(".orphaned_at marker present")

if cache_ok:
    passed += 1
    print("[PASS] T10: Cache synced (4 key files match, no orphan marker)")
else:
    print("[FAIL] T10: Cache issues")

# SUMMARY
print()
print("=" * 60)
print("RESULTS: %d/10 PASSED | %d ERRORS | %d WARNINGS" % (passed, len(errors), len(warnings)))
if errors:
    for e in errors:
        print("  [ERROR] %s" % e)
if warnings:
    for w in warnings:
        print("  [WARN] %s" % w)
if passed == 10:
    print()
    print("ALL TESTS PASSED")
print("=" * 60)
