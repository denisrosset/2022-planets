# Telemetry and user experiments

You can always install the binaries without any telemetry: https://github.com/VSCodium/vscodium, 
though I don't have much experience with them.

## "Leave me alone" defaults

For the standard VS Code releases, add in the main `settings.json`:

```json
    "python.experiments.enabled": false,
    "telemetry.telemetryLevel": "off",
    "workbench.enableExperiments": false,
```

see https://code.visualstudio.com/docs/getstarted/telemetry