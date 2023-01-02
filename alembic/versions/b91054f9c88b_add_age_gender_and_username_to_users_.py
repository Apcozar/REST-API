"""add age, gender and username to Users table

Revision ID: b91054f9c88b
Revises: 
Create Date: 2023-01-02 12:22:16.488339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b91054f9c88b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', 
        sa.Column('username', sa.String(length=20), unique=True, nullable=False))

    op.add_column('users', 
        sa.Column('age', sa.Integer, nullable=False))
    
    op.add_column('users', 
        sa.Column('gender', sa.String(length=20), nullable=False))

    op.alter_column('users', 'name', 
        existing_type=sa.String,
        type_=sa.String(length=40))

    op.alter_column('users', 'surname', 
        existing_type=sa.String,
        type_=sa.String(length=40))

    op.drop_column('users', 'description')

def downgrade():
    op.drop_column('users','username')
    op.drop_column('users','age')
    op.drop_column('users','gender')

    op.alter_column('users', 'name', 
        existing_type=sa.String(length=40),
        type_=sa.String)

    op.alter_column('users', 'surname', 
        existing_type=sa.String(length=40),
        type_=sa.String)

    op.add_column('users',
        sa.Column('description', sa.String(length=50), nullable=False))