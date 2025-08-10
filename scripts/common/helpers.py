import subprocess

from pathlib import Path

from .github import Github

def dump_build_notes(name: str, working_dir: Path, output: Path, contents: list[str]):
    # Check if the source directory is a git one, if so we can add some cool
    # git information to the output directory for storage later.
    try:
        remote = subprocess.check_output(
            ["git", "remote", "get-url", "origin"], text=True, cwd=working_dir
        ).strip()
        commit_hash = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True, cwd=working_dir
        ).strip()

        note_text = f"""# {name}

Compiled from `{remote}`:`{commit_hash}`

Contains:

"""
        note_text += "\n".join(contents)
        output.write_text(note_text)

    except Exception as e:
        # Not a git directory or some other failure, don't need to fail anything though
        Github.notice(
            f"Skipping git information for {working_dir} due to exception: {e}"
        )
        pass
