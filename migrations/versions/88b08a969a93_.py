"""empty message

Revision ID: 88b08a969a93
Revises: 
Create Date: 2023-05-08 17:30:20.103130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88b08a969a93'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('event_id', sa.BigInteger(), nullable=False),
    sa.Column('event_title', sa.String(length=256), nullable=False),
    sa.Column('event_venue', sa.String(length=256), nullable=False),
    sa.Column('event_address', sa.String(length=256), nullable=False),
    sa.Column('event_state', sa.String(length=250), nullable=False),
    sa.Column('event_district', sa.String(length=256), nullable=False),
    sa.Column('event_date', sa.String(length=128), nullable=False),
    sa.Column('event_time', sa.String(length=128), nullable=False),
    sa.Column('created_by', sa.String(length=120), nullable=False),
    sa.Column('created_on', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('event_id')
    )
    op.create_table('pincodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('circle', sa.String(), nullable=False),
    sa.Column('delivery', sa.String(), nullable=False),
    sa.Column('district', sa.String(), nullable=False),
    sa.Column('division', sa.String(), nullable=False),
    sa.Column('latitude', sa.String(), nullable=False),
    sa.Column('longitude', sa.String(), nullable=False),
    sa.Column('office', sa.String(), nullable=False),
    sa.Column('office_type', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('pin', sa.String(), nullable=False),
    sa.Column('region', sa.String(), nullable=False),
    sa.Column('state_id', sa.String(), nullable=False),
    sa.Column('related_headoffice', sa.String(), nullable=False),
    sa.Column('related_suboffice', sa.String(), nullable=False),
    sa.Column('taluk', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tokenblocklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('tokenblocklist', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_tokenblocklist_jti'), ['jti'], unique=False)

    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('feedback',
    sa.Column('feedback_id', sa.Integer(), nullable=False),
    sa.Column('question1', sa.String(), nullable=True),
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.event_id'], ),
    sa.PrimaryKeyConstraint('feedback_id')
    )
    op.create_table('participants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=False),
    sa.Column('designation', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('mobilenumber', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('district', sa.String(), nullable=False),
    sa.Column('block', sa.String(), nullable=False),
    sa.Column('grampanchayat', sa.String(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.event_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participants')
    op.drop_table('feedback')
    op.drop_table('users')
    with op.batch_alter_table('tokenblocklist', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tokenblocklist_jti'))

    op.drop_table('tokenblocklist')
    op.drop_table('pincodes')
    op.drop_table('events')
    # ### end Alembic commands ###
