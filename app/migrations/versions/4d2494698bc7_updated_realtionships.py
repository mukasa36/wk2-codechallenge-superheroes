"""updated realtionships

Revision ID: 4d2494698bc7
Revises: f9c6c6fb5cc5
Create Date: 2023-10-02 08:30:32.358616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d2494698bc7'
down_revision = 'f9c6c6fb5cc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.alter_column('strength',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('hero_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('power_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.alter_column('power_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('hero_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('strength',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
