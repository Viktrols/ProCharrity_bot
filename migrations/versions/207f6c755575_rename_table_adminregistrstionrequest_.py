"""rename table AdminRegistrstionRequest

Revision ID: 207f6c755575
Revises: f4f995589943
Create Date: 2021-09-14 19:37:39.507204

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '207f6c755575'
down_revision = 'f4f995589943'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('admin_registration_requests', 'admin_token_requests')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('admin_token_requests', 'admin_registration_requests')
