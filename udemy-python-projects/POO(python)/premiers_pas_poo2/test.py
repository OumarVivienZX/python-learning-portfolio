import typer
from typing import Optional
from pathlib import Path

app = typer.Typer()


@app.command('run')
def main(extension: str,
         directory: Optional[str] = typer.Argument( None, help="Dossier dans lequel chercher."),
         delete: bool = typer.Option(False, help="Supprimes le fichiers trouvés")):
    """
    Affiche les fichiers trouvés avec l'extension donnée
    """

    if directory:
        directory_path = Path(directory)
    else:
        directory_path = Path.cwd()

    if not directory_path.exists():
        typer.secho(f"Le dossier '{directory_path}'  n'existe pas ", fg=typer.colors.RED, )
        raise typer.Exit()

    files = directory_path.rglob(f"*.{extension}")

    if delete:
        typer.confirm("Voulez-vous supprimer?", abort=True)
        for file in files:
            file.unlink()
            typer.secho("Suppression du fichier {file}", fg=typer.colors.RED)
    else:
        typer.secho(f"fichiers  touvés avec l'extension {extension}", bg=typer.colors.BLUE,
                    fg=typer.colors.BRIGHT_WHITE)
        for file in files:
            typer.echo(file)


@app.command()
def search(extension: str = ""):
    main(extension=extension, directory=None, delete=False)


@app.command()
def delete(extension: str = ""):
    main(extension=extension, directory=None, delete=True)


if __name__ == "__main__":
    app()