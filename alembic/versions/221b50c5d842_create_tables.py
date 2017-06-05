"""create tables

Revision ID: 221b50c5d842
Revises: 
Create Date: 2017-06-05 15:19:09.646455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '221b50c5d842'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Admin_user',
        sa.Column('id', sa.Integer, primary_key=True,autoincrement=True),
        sa.Column('username', sa.String(64), nullable=False),
        sa.Column('password', sa.String(128))
    )

def downgrade():
    op.drop_table('Admin_user')