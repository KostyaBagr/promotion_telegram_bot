"""creted models

Revision ID: 38b44b204403
Revises: 
Create Date: 2024-01-23 16:55:00.127130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38b44b204403'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('additional_posts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('file', sa.String(), nullable=True),
    sa.Column('file_type', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_additional_posts_id'), 'additional_posts', ['id'], unique=False)
    op.create_table('contact_me',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_contact_me_id'), 'contact_me', ['id'], unique=False)
    op.create_table('posts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('file', sa.String(), nullable=True),
    sa.Column('audio', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_id'), 'posts', ['id'], unique=False)
    op.create_table('referral_links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_referral_links_id'), 'referral_links', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('telegram_id', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_telegram_id'), 'users', ['telegram_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_telegram_id'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_referral_links_id'), table_name='referral_links')
    op.drop_table('referral_links')
    op.drop_index(op.f('ix_posts_id'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_contact_me_id'), table_name='contact_me')
    op.drop_table('contact_me')
    op.drop_index(op.f('ix_additional_posts_id'), table_name='additional_posts')
    op.drop_table('additional_posts')
    # ### end Alembic commands ###
