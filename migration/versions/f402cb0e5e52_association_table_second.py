"""association table second

Revision ID: f402cb0e5e52
Revises: 54398735b422
Create Date: 2023-06-07 23:48:20.395218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f402cb0e5e52'
down_revision = '54398735b422'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('barbershop_id', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.create_foreign_key(None, 'reviews', 'barbershops', ['barbershop_id'], ['id'])
    op.drop_column('reviews', 'babershop_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('babershop_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.create_foreign_key(None, 'reviews', 'barbershops', ['babershop_id'], ['id'])
    op.drop_column('reviews', 'barbershop_id')
    # ### end Alembic commands ###
