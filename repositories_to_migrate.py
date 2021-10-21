FNAL_REDMINE_REPOS = [
    "cetlib_except",
    "cetlib",
    "hep_concurrency",
    "fhicl",
    "fhicl-cpp",
    "fhicl-py",
    "messagefacility",
    "canvas",
    "canvas_root_io",
    "art",
    "art_root_io",
    "gallery",
    "critic",
    "ifdh-art",
    "mrb",
    "cetbuildtools",
    "studio",
]

GITHUB_ORG = "test-art-framework-suite"
GITHUB_ORG_REPOS = map(lambda name: name.replace("_", "-"), FNAL_REDMINE_REPOS)
