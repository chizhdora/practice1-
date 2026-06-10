"""add description to territories

Revision ID: 002
Revises: aae1847b9d15
Create Date: 2026-06-10
"""
from alembic import op
import sqlalchemy as sa

revision = '002'
down_revision = 'aae1847b9d15'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('territories', sa.Column('description', sa.String(500), nullable=True))

def downgrade():
    op.drop_column('territories', 'description')