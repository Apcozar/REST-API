"""set constraint to not set ourselfs as friends

Revision ID: d7c577ac0c4b
Revises: b91054f9c88b
Create Date: 2023-01-02 22:44:28.766288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7c577ac0c4b'
down_revision = 'b91054f9c88b'
branch_labels = None
depends_on = None


def upgrade() -> None:
   op.create_check_constraint(
    "ck_not_same_person",
    "friendships",
    "user_id != friend_id" 
    )


def downgrade() -> None:
    op.drop_constraint("ck_not_same_person",
    "friendships")
