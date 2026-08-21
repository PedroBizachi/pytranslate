# pytranslate

[EDIT] A super-simple cli translation tool

## Roadmap

- [x] Translate text
- [x] Accept input from terminal
  - [-] 2 args runs with source=auto target=arg1 text=arg2
  - [-] 3 args runs with source=arg1 target=arg2 text=arg3
- [x] Pre-defined user configurations
  - [ ] Uses GoogleTranslate by default, user can change it in the settings
  - [ ] Users can configure their own pro API to activate some extra translators
- [ ] Build a beautifull TUI using Textual inspired on HyprMon
  - [ ] 2 tabs, first for translation and second for configurations
  - [ ] Layout inspired on Google/Deepl Translate
  - [ ] "Hot Reload" feature
  - [ ] AI tab with "deep-translator\[ai]"
- [ ] Keep cli to translate docx and pdf files

## Future changes

- [ ] Test the performance between deep_translator package and API
- [ ] Change from source/target flags to positional arguments
  - [ ] Must accept only one `@click.argument(nargs=-1)` and handle the source/target inside the code
  - [ ] Can check first arg comparing to `"auto"` or `translator.is_language_supported`
  - [ ] Can check second arg with `translator.is_language_supported`
