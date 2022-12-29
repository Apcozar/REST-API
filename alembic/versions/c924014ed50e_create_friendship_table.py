"""create friendship table

Revision ID: c924014ed50e
Revises: 
Create Date: 2022-12-29 12:39:06.106886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c924014ed50e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("friendship",
    sa.Column("user_id", sa.Integer(), nullable=False),
    sa.Column("friend_id", sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
    sa.ForeignKeyConstraint(["friend_id"], ["user.ir"], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint("user_id", "friend_id")
    )
    


def downgrade() -> None:
    op.drop_table("friendship")
