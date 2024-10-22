"""Create book model

Revision ID: 0919d9efd5ea
Revises: 
Create Date: 2024-09-11 19:47:54.671666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0919d9efd5ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
