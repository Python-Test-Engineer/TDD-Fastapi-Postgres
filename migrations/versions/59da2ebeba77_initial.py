"""initial

Revision ID: 59da2ebeba77
Revises: 
Create Date: 2024-04-11 17:01:49.316376

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59da2ebeba77'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attribute',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.CheckConstraint('LENGTH(name) > 0', name='attribute_name_length_check'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='uq_attribute_name')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=120), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('level', sa.Integer(), server_default='100', nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.CheckConstraint('LENGTH(name) > 0', name='category_name_length_check'),
    sa.CheckConstraint('LENGTH(slug) > 0', name='category_slug_length_check'),
    sa.ForeignKeyConstraint(['parent_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'level', name='uq_category_name_level'),
    sa.UniqueConstraint('slug', name='uq_category_slug')
    )
    op.create_table('product_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.CheckConstraint('LENGTH(name) > 0', name='product_type_name_length_check'),
    sa.ForeignKeyConstraint(['parent_id'], ['product_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'level', name='uq_product_type_name_level')
    )
    op.create_table('seasonal_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.CheckConstraint('LENGTH(name) > 0', name='seasonal_event_name_length_check'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='uq_seasonal_event_name')
    )
    op.create_table('attribute_value',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('attribute_value', sa.String(length=100), nullable=False),
    sa.Column('attribute_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('LENGTH(attribute_value) > 0', name='attribute_value_name_length_check'),
    sa.ForeignKeyConstraint(['attribute_id'], ['attribute.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('attribute_value', 'attribute_id', name='uq_attribute_value_attribute_id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pid', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('slug', sa.String(length=220), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_digital', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('stock_status', sa.Enum('oos', 'is', 'obo', name='status_enum'), server_default='oos', nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('seasonal_id', sa.Integer(), nullable=True),
    sa.CheckConstraint('LENGTH(name) > 0', name='product_name_length_check'),
    sa.CheckConstraint('LENGTH(slug) > 0', name='product_slug_length_check'),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['seasonal_id'], ['seasonal_event.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='uq_product_name'),
    sa.UniqueConstraint('pid', name='uq_product_pid'),
    sa.UniqueConstraint('slug', name='uq_product_slug')
    )
    op.create_table('product_line',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=5, scale=2), nullable=False),
    sa.Column('sku', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('stock_qty', sa.Integer(), server_default='0', nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('"order" >= 1 AND "order" <= 20', name='product_order_line_range'),
    sa.CheckConstraint('price >= 0 AND price <= 999.99', name='product_line_max_value'),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('order', 'product_id', name='uq_product_line_order_product_id'),
    sa.UniqueConstraint('sku', name='uq_product_line_sku')
    )
    op.create_table('product_product_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_type_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['product_type_id'], ['product_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_type_id', 'product_id', name='uq_product_id_product_type_id')
    )
    op.create_table('product_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alternative_text', sa.String(length=100), nullable=False),
    sa.Column('url', sa.String(length=100), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('product_line_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('"order" >= 1 AND "order" <= 20', name='product_image_order_range'),
    sa.CheckConstraint('LENGTH(alternative_text) > 0', name='product_image_alternative_length_check'),
    sa.CheckConstraint('LENGTH(url) > 0', name='product_image_url_length_check'),
    sa.ForeignKeyConstraint(['product_line_id'], ['product_line.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('order', 'product_line_id', name='uq_product_image_order_product_line_id')
    )
    op.create_table('product_line_attribute_value',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('attribute_value_id', sa.Integer(), nullable=False),
    sa.Column('product_line_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['attribute_value_id'], ['attribute_value.id'], ),
    sa.ForeignKeyConstraint(['product_line_id'], ['product_line.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('attribute_value_id', 'product_line_id', name='uq_product_line_attribute_value')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_line_attribute_value')
    op.drop_table('product_image')
    op.drop_table('product_product_type')
    op.drop_table('product_line')
    op.drop_table('product')
    op.drop_table('attribute_value')
    op.drop_table('seasonal_event')
    op.drop_table('product_type')
    op.drop_table('category')
    op.drop_table('attribute')
    # ### end Alembic commands ###
