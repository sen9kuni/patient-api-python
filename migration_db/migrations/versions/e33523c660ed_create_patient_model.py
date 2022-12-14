"""Create patient model

Revision ID: e33523c660ed
Revises: 
Create Date: 2022-11-25 22:53:13.351956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e33523c660ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=225), nullable=False),
    sa.Column('last_name', sa.String(length=225), nullable=False),
    sa.Column('birth', sa.DateTime(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patient')
    # ### end Alembic commands ###
