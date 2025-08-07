# SS14 Native-Build

A collection of submodules providing dependencies for building [Space Station 14](https://github.com/space-wizards/space-station-14).

Building is handled through the `Build Natives` workflow action and relies on Github's runners to perform the actual compilation.
Local building is possible by running your platform's python file under the [scripts](./scripts/) directory. Though you will need to make sure you have all dependencies setup to actually build. Consult the [workflow](./.github/workflows/build.yml) file for your platform and see what's installed from the `Install Deps` step.

Each platform produces an zip file containing all relevant shared libs for it, any debug symbols, and a `notes.md` giving information on where and what commit the code came from.
