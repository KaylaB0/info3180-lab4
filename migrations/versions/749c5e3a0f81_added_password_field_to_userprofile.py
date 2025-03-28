"""Added password field to UserProfile

Revision ID: 749c5e3a0f81
Revises: 2c46f90743fa
Create Date: 2025-03-15 19:43:02.500166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '749c5e3a0f81'
down_revision = '2c46f90743fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
