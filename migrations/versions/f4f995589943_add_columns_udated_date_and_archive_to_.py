"""add columns udated_date and archive to ReasonCancelling table

Revision ID: f4f995589943
Revises: 0ea530c95a28
Create Date: 2021-09-11 18:25:25.991086

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f4f995589943'
down_revision = '0ea530c95a28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reasons_canceling', sa.Column('updated_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    op.add_column('reasons_canceling', sa.Column('archive', sa.Boolean(), server_default=sa.text('false'), nullable=False))
    op.alter_column('reasons_canceling', 'added_date', existing_type=postgresql.TIMESTAMP(),
                    type_=sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reasons_canceling', 'archive')
    op.drop_column('reasons_canceling', 'updated_date')
    op.alter_column('reasons_canceling', 'added_date', existing_type=sa.TIMESTAMP(),
                    type_=postgresql.TIMESTAMP(), nullable=False)
    # ### end Alembic commands ###
