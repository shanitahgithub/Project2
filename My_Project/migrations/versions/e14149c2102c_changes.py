"""changes

Revision ID: e14149c2102c
Revises: 05d483886a91
Create Date: 2024-07-06 12:45:24.864837

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e14149c2102c'
down_revision = '05d483886a91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payments')
    op.drop_table('transactions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('orderItem_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('status', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('transaction_amount', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['orderItem_id'], ['order_item.id'], name='transactions_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='transactions_ibfk_2', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('payments',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('order_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('amount', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('payment_date', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('payment_method', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('status', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name='payments_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='payments_ibfk_2', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
