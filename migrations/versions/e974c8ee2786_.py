"""empty message

Revision ID: e974c8ee2786
Revises: e01097823b77
Create Date: 2020-04-10 16:55:58.758368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e974c8ee2786'
down_revision = 'e01097823b77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password_digest', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('shelves', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'shelves', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shelves', type_='foreignkey')
    op.drop_column('shelves', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
