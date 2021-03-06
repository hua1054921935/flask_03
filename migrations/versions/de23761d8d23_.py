"""empty message

Revision ID: de23761d8d23
Revises: f1bb4e08acc3
Create Date: 2018-01-29 15:40:14.222843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de23761d8d23'
down_revision = 'f1bb4e08acc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('info', sa.String(length=16), nullable=True))
    op.add_column('users', sa.Column('info', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'info')
    op.drop_column('roles', 'info')
    # ### end Alembic commands ###
