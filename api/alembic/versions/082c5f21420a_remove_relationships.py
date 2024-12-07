"""remove relationships

Revision ID: 082c5f21420a
Revises: 
Create Date: 2024-12-07 16:38:17.449278

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '082c5f21420a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_ForecastsHeader_id', table_name='ForecastsHeader')
    op.drop_table('ForecastsHeader')
    op.drop_index('ix_Forecasts_id', table_name='Forecasts')
    op.drop_table('Forecasts')
    op.drop_index('ix_Units_id', table_name='Units')
    op.drop_table('Units')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Units',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('modelrun', sa.VARCHAR(), nullable=False),
    sa.Column('precipitation', sa.VARCHAR(), nullable=True),
    sa.Column('windspeed', sa.VARCHAR(), nullable=True),
    sa.Column('precipitation_probability', sa.VARCHAR(), nullable=True),
    sa.Column('relativehumidity', sa.VARCHAR(), nullable=True),
    sa.Column('temperature', sa.VARCHAR(), nullable=True),
    sa.Column('time', sa.VARCHAR(), nullable=True),
    sa.Column('pressure', sa.VARCHAR(), nullable=True),
    sa.Column('winddirection', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_Units_id', 'Units', ['id'], unique=False)
    op.create_table('Forecasts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('modelrun', sa.VARCHAR(), nullable=False),
    sa.Column('date_forecast', sa.VARCHAR(), nullable=True),
    sa.Column('windspeed', sa.FLOAT(), nullable=True),
    sa.Column('temperature', sa.FLOAT(), nullable=True),
    sa.Column('precipitation_probability', sa.FLOAT(), nullable=True),
    sa.Column('convective_precipitation', sa.FLOAT(), nullable=True),
    sa.Column('rainspot', sa.VARCHAR(), nullable=True),
    sa.Column('pictocode', sa.FLOAT(), nullable=True),
    sa.Column('felttemperature', sa.FLOAT(), nullable=True),
    sa.Column('precipitation', sa.FLOAT(), nullable=True),
    sa.Column('isdaylight', sa.FLOAT(), nullable=True),
    sa.Column('uvindex', sa.FLOAT(), nullable=True),
    sa.Column('relativehumidity', sa.FLOAT(), nullable=True),
    sa.Column('sealevelpressure', sa.FLOAT(), nullable=True),
    sa.Column('winddirection', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_Forecasts_id', 'Forecasts', ['id'], unique=False)
    op.create_table('ForecastsHeader',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('modelrun', sa.VARCHAR(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('height', sa.INTEGER(), nullable=True),
    sa.Column('timezone_abbrevation', sa.VARCHAR(), nullable=True),
    sa.Column('latitude', sa.INTEGER(), nullable=True),
    sa.Column('modelrun_utc', sa.VARCHAR(), nullable=True),
    sa.Column('longitude', sa.INTEGER(), nullable=True),
    sa.Column('utc_timeoffset', sa.INTEGER(), nullable=True),
    sa.Column('generation_time_ms', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_ForecastsHeader_id', 'ForecastsHeader', ['id'], unique=False)
    # ### end Alembic commands ###