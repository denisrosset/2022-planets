# Installing VS Code

(Information current as of March 8, 2022)

Download from the main page: https://code.visualstudio.com and install. A few details below.
We also comment on differences between platforms below.

## On Linux

There are .deb files for Debian/Ubuntu, and packages for the RedHat ecosystem (RHEL, Fedora, CentOS)
As a general principle, I avoid Snap packages due to extensions possibly conflicting with the
Snap sandboxing.

* https://code.visualstudio.com/docs/setup/linux

Setting to obtain a {ref}`compact title bar <appearance/title_bar>`.

## On Mac

* https://code.visualstudio.com/docs/setup/mac

VS Code asking for permissions: it is fine to deny access. One should avoid working on project
folders that are direct children of the `$HOME` folder.

See further info:

* https://code.visualstudio.com/docs/setup/mac#_mojave-privacy-protections

* https://github.com/microsoft/vscode/issues/55236


## On Windows

I don't use Windows and neither my immediate colleagues, but here is what I can say.

Prefer the "user setup" option, so that VS Code is installed in your User folder without
requiring administrator privileges. Subsequent updates will also be smoother.

* https://code.visualstudio.com/docs/setup/windows
