import subprocess

from .platform import Platform
from .software import Software, SoftwareOutput
from .github import Github

def separate_debug_info(build: Software):
    # Strip debug information out per build's outputs
    new_outputs = []
    for output in build.outputs[Platform.Linux]:
        output_name = SoftwareOutput.get_dst_name(output)
        Github.log(f"Moving debug information for {output_name}")
        debug_name = f"{output_name}.debug"
        subprocess.run(
            [
                "objcopy",
                "--only-keep-debug",
                str(build.publish_dir.joinpath(output_name)),
                str(build.publish_dir.joinpath(debug_name)),
            ],
            check=True
        )

        subprocess.run(
            [
                "strip",
                str(build.publish_dir.joinpath(output_name)),
            ],
            check=True
        )
        new_outputs.append(debug_name)


    build.outputs[Platform.Linux].extend(new_outputs)
