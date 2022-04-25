# Spell checking

Visual Studio code does not include spell checking out of the box. We already installed the
[Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
extension.

To avoid having the spelling mistakes as compilation errors, add this line to your user settings:

```json
    "cSpell.diagnosticLevel": "Hint",
```

Check the [documentation](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
on how to include unknown words in your user or project dictionary.
