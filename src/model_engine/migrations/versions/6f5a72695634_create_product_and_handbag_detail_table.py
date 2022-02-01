"""create product and handbag_detail table

Revision ID: 6f5a72695634
Revises: 
Create Date: 2022-02-01 11:27:13.309768

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6f5a72695634'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'pd_product',
        sa.Column('install_ts', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('update_ts', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('created_by_id', sa.Integer(), nullable=True),
        sa.Column('updated_by_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('type', postgresql.ENUM('CLOTHING', 'ACCESSORIES', name='type', create_type=False), nullable=False),
        sa.Column('meta', sa.JSON()),
        sa.Column('description', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )

    op.create_table(
        'pd_handbag_detail',
        sa.Column('install_ts', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('update_ts', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('created_by_id', sa.Integer(), nullable=True),
        sa.Column('updated_by_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('meta', sa.JSON()),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('type', postgresql.ENUM('HANDBAGS', 'WATCHES', 'JEWELLERY', name='type', create_type=False), nullable=False),
        sa.ForeignKeyConstraint(
            ['product_id'],
            ['pd_product.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('pd_product')
    op.drop_table('pd_handbag_detail')
