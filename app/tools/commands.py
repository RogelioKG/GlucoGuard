# third party library
import click
from flask.cli import AppGroup
from tqdm import tqdm

# local library
from app import db
from app.models.volunteer import Volunteer
from app.models import BaseDataModel


# Flask CLI 指令群
db_cli = AppGroup("db", help="Manipulate data in database.")


@db_cli.command("clear", help="Clear all data in database.")
def clear():
    """Clear all data in database."""
    db.drop_all()
    db.create_all()
    click.echo("Cleared all data in database.")


@db_cli.command("generate", help="Generate mock data.")
@click.option(
    "--volunteer",
    "table",
    type=click.UNPROCESSED,
    flag_value=Volunteer,
    help="Table: Volunteer",
)
@click.argument("numbers", type=int)
def generate_volunteer(table: BaseDataModel, numbers: int):
    """Generate mock data."""
    for mock_data in tqdm(table.generate(numbers), total=numbers, colour="green", unit="data"):
        db.session.add(mock_data)
    db.session.commit()
    click.echo(f"Generated {numbers} mock data of {table.__tablename__}.")
