"""changed year back to integer type

Revision ID: 46ccedcfd75f
Revises: 1e1560bcc541
Create Date: 2022-12-06 15:22:03.187738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46ccedcfd75f'
down_revision = '1e1560bcc541'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.alter_column('year',
               existing_type=sa.VARCHAR(length=4),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.alter_column('year',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=4),
               existing_nullable=False)

    # ### end Alembic commands ###