# CrimsonGlass vOS
CrimsonGlass is a Virtual Operating System, meaning it runs on top of another, simpler OS, usually Linux.

## Package Manager
CrimsonGlass uses the custom `pakd` package manager, built for **Docswim**, another vOS.

You can download and install packages and apps using `pakd install <package_name>`.
To publish a package, you must first fill up the Package Publishing form at `PUBLISH.md` and create an issue with it,
then I will check the package and, if it is OK, will add it to the `pakd list`.

## User Guide
For the normal user, if a command is not available in the OS, you can easily use `subos <command> <args>` to run the command with the specified arguments in the underlying OS console.
While the commands CrimsonGlass has aren't enough, `subos` will be useful, when CrimsonGlass has lots of commands, `subos` may not be as useful, but still useful.

If you need to run Python code, you can use `pyeval <expression>` to run it INSIDE the CrimsonGlass process, YOU CAN BREAK THINGS BY RUNNING SOME CODE, BE CAREFUL.

## Developer Guide
For developers, to create a package or application, you can use built-in features, or write it in Python 3.
The package just has to define a function called `def run(args)` and it will be called when using the command `<app_name> <args>`.

## Connction with `DocswimOS`
Docswim is the Graphical Virtual OS I'm building, it also uses the `pakd` package manager, but is built in Java.
