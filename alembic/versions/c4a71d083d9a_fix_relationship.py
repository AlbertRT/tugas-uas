"""fix relationship

Revision ID: c4a71d083d9a
Revises: 3adce8661f9c
Create Date: 2025-05-31 12:56:55.583189

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'c4a71d083d9a'
down_revision: Union[str, None] = '3adce8661f9c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('login_history')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', mysql.VARCHAR(length=12), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('username', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('role', mysql.ENUM('admin', 'user'), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('login_history',
    sa.Column('id', mysql.VARCHAR(length=12), nullable=False),
    sa.Column('user_id', mysql.VARCHAR(length=12), nullable=True),
    sa.Column('logout_date', mysql.DATETIME(), nullable=True),
    sa.Column('device_id', mysql.VARCHAR(length=12), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('login_history_ibfk_1')),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
