"""empty message

Revision ID: a87abc758a5c
Revises: 1ab214a49709
Create Date: 2022-01-08 14:41:24.080731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a87abc758a5c'
down_revision = '1ab214a49709'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member', sa.Column('location', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('member', 'location')
    # ### end Alembic commands ###
