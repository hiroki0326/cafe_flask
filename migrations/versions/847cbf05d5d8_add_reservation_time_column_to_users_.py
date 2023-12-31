"""Add reservation_time column to users table

Revision ID: 847cbf05d5d8
Revises: 772f27da5ac4
Create Date: 2023-07-05 16:10:42.334863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '847cbf05d5d8'
down_revision = '772f27da5ac4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reservation_date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('reservation_time', sa.Time(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.drop_column('reservation_time')
        batch_op.drop_column('reservation_date')

    # ### end Alembic commands ###
