"""added field telegram_id to user table

Revision ID: 33b581594c5b
Revises: 312de01fefb6
Create Date: 2024-01-11 14:39:54.909360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33b581594c5b'
down_revision: Union[str, None] = '312de01fefb6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('telegram_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_users_telegram_id'), 'users', ['telegram_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_telegram_id'), table_name='users')
    op.drop_column('users', 'telegram_id')
    # ### end Alembic commands ###