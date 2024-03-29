"""updated contanc me table

Revision ID: b8e4e625f83a
Revises: 38b44b204403
Create Date: 2024-01-23 16:57:44.209242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8e4e625f83a'
down_revision: Union[str, None] = '38b44b204403'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'contact_me', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contact_me', type_='unique')
    # ### end Alembic commands ###
