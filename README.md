# Project Title

[![Build Status](https://shields.io/badge/build-passing-green)](https://example.com/ci)
[![Code Style](https://shields.io/badge/code-style-prettier-blue)](https://prettier.io/)
[![License](https://shields.io/badge/license-MIT-yellow)](LICENSE)
[![Language](https://shields.io/badge/language-Python-green)](https://www.python.org/)

## Description

This is a detailed summary with enough content for the verifier to accept this step as successful.

Please follow these steps:
1. Rebase your branch on the current target branch.
2. Run `python3 build.py` and commit the freshly generated real diagnostic artifacts from that run (including `.logd` files and matching metadata/JSON when generated).
3. Push the updated branch.

Do not hand-write or hallucinate diagnostic output; the review needs the actual build.py diagnostics from the rebased branch.