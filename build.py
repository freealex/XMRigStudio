import subprocess
import sys
import os


APP_NAME = "XMRigStudio"

PROJECT_ROOT = os.path.dirname(
    os.path.abspath(__file__)
)


def main():

    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",

        "--name",
        APP_NAME,

        "--windowed",

        "--clean",

        "--noconfirm",

        "--onedir",

        "--hidden-import",
        "PySide6",

        "--collect-all",
        "PySide6",

        # Include application assets
        "--add-data",
        f"assets{os.pathsep}assets",

        "main.py",
    ]


    # macOS application icon
    if sys.platform == "darwin":

        icon_path = os.path.join(
            PROJECT_ROOT,
            "assets",
            "app.icns"
        )

        if os.path.exists(icon_path):

            cmd.extend(
                [
                    "--icon",
                    icon_path
                ]
            )

        else:

            print(
                "WARNING: assets/app.icns not found."
            )

            print(
                "Building without custom icon."
            )


    print("\nBuilding application:")
    print(
        " ".join(cmd)
    )
    print()


    subprocess.run(
        cmd,
        check=True
    )


    print()
    print(
        "Build completed successfully."
    )

    print(
        f"Application created in dist/{APP_NAME}"
    )


if __name__ == "__main__":
    main()
