"""create test_python table

Revision ID: 554beb601819
Revises: 
Create Date: 2019-10-15 22:13:13.867146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '554beb601819'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'test_python',
        sa.Column('id', sa.Integer(), primary_key=True,nullable=True,autoincrement=True),
        sa.Column('sum', sa.Float, nullable=True),
        sa.Column('start', sa.types.DateTime(timezone=True),nullable=True),
        sa.Column('end', sa.types.DateTime(timezone=True),nullable=True),
        sa.Column('iterations', sa.Integer(),nullable=True),
    )

def downgrade():
    op.drop_table('test_python')
