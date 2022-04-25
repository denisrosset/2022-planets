(settings)=
# How are settings managed

Visual Studio looks at settings in two places:

- the user `settings.json` file
- the project `.vscode/settings.json` file

## User JSON settings

Visual Studio has a main configuration file, that can be accessed using a command.

In `settings.json`, accessible using CTRL+SHIFT+P `Preferences: Open Settings (JSON)`

Note: on Mac, the CTRL+SHIFT+P shortcut for to "Show Command Palette" is CMD+SHIFT+P or F1 (all platforms).

Settings can also be edited from the `File` > `Preferences` > `Settings` menu (Windows/Linux) or from
 `Code` > `Preferences` > `Settings` (Mac).
 
## Per-project settings

To work with a Python project, one opens the root folder of that project in VS Code. The root
folder usually contains the `.git` subfolder as well.

Add a `settings.json` file in a `.vscode` subfolder of the root folder; this is where you'll
put per-project settings, such as Python environment options and style parameters.

## Learn more

- https://code.visualstudio.com/docs/getstarted/settings
