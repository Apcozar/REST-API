"""create is_admin field

Revision ID: 7647a500e6ae
Revises: d7c577ac0c4b
Create Date: 2023-01-03 11:32:24.941360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7647a500e6ae'
down_revision = 'd7c577ac0c4b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users',
    sa.Column('is_admin', sa.Boolean, nullable=False, default=False))
    

def downgrade() -> None:
    op.drop_column('users', 'is_admin')
