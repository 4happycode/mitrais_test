"""create users table

Revision ID: f48ebf68c2c5
Revises: 
Create Date: 2021-09-02 11:31:24.710536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f48ebf68c2c5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('firstname', sa.String(100), nullable=True),
        sa.Column('lastname', sa.String(100), nullable=True),
        sa.Column('phone', sa.String(20), nullable=True),
        sa.Column('email', sa.String(100), nullable=True),
        sa.Column('gender', sa.String(50), nullable=True),
        sa.Column('datebirth', sa.Date(), nullable=True)
    )
    pass


def downgrade():
    pass
