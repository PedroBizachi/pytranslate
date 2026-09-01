# Roadmap

## v1

- [x] Translate text
- [x] Accept input from terminal
  - [-] 2 args runs with source=auto target=arg1 text=arg2
  - [-] 3 args runs with source=arg1 target=arg2 text=arg3
- [x] Pre-defined user configurations
- [x] Build a beautiful TUI using Textual inspired on Posting, LazyGit, HyprMon, etc.
  - [x] Layout inspired on Google/Deepl Translate
  - [x] "Hot Reload" feature
  - [x] Keymap to change source/target languages
  - [ ] Keymap to copy translated text

## v2

- [ ] Make settings tab
  - [ ] 2 tabs, first for translation and second for configurations
  - [ ] Users can modify the translator engine
  - [ ] Users can configure their own pro API to activate some extra translators
- [ ] AI tab with "deep-translator\[ai]"
- [ ] Keep cli to only translate docx and pdf files
- [ ] Add spell checker (pyspellchecker)

## Future optimizations

- [ ] Test the performance between deep_translator package and API
- [ ] Improve logic
