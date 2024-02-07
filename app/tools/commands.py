# third party library
import click
from flask.cli import AppGroup

# local library
from app import db
from app.models.volunteer import Volunteer
from app.tools import generate


# Flask CLI 指令群
db_cli = AppGroup("db", help="Manipulate data in database.")


@db_cli.command("clear", help="Clear all data in database.")
def clear():
    db.drop_all()
    db.create_all()
    click.echo("Cleared all data in database.")


@db_cli.command("generate-volunteers", help="Generate mock data of volunteers.")
@click.argument("numbers", type=int)
def generate_volunteer(numbers: int):

    volunteers = []
    for _ in range(numbers):
        volunteer = Volunteer(generate.random_form())
        volunteer.predict()
        volunteers.append(volunteer)

    db.session.add_all(volunteers)
    db.session.commit()

    click.echo(f"Generated {numbers} mock data of volunteers.")
