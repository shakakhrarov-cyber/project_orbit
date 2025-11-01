from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = 'initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create users table
    op.create_table(
        'users',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('email', sa.String(255), nullable=True)
    )
    
    # Create sessions table
    op.create_table(
        'sessions',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=True),
        sa.Column('state_vector', sa.JSON(), nullable=True),
        sa.Column('covariance', sa.JSON(), nullable=True),
        sa.Column('answered_qids', sa.JSON(), nullable=False, server_default='[]'),
        sa.Column('status', sa.String(20), nullable=False, server_default='active'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('completed_at', sa.DateTime(), nullable=True)
    )
    
    # Create questions table
    op.create_table(
        'questions',
        sa.Column('id', sa.String(50), primary_key=True),
        sa.Column('text', sa.Text(), nullable=False),
        sa.Column('type', sa.String(20), nullable=False),
        sa.Column('options', sa.JSON(), nullable=True),
        sa.Column('targets', sa.JSON(), nullable=True),
        sa.Column('info_weight', sa.JSON(), nullable=True),
        sa.Column('difficulty', sa.String(), nullable=False, server_default='1.0'),
        sa.Column('locale', sa.String(10), nullable=False, server_default='en'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False)
    )
    
    # Create responses table
    op.create_table(
        'responses',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('session_id', UUID(as_uuid=True), sa.ForeignKey('sessions.id'), nullable=False),
        sa.Column('question_id', sa.String(50), sa.ForeignKey('questions.id'), nullable=False),
        sa.Column('payload', sa.JSON(), nullable=False),
        sa.Column('latency_ms', sa.String(), nullable=True),
        sa.Column('timestamp', sa.DateTime(), nullable=False)
    )
    
    # Create archetypes table
    op.create_table(
        'archetypes',
        sa.Column('id', sa.String(50), primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('vector', sa.JSON(), nullable=False),
        sa.Column('min_requirements', sa.JSON(), nullable=True),
        sa.Column('contraindications', sa.JSON(), nullable=True),
        sa.Column('resources', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False)
    )
    
    # Create match_reports table
    op.create_table(
        'match_reports',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('session_id', UUID(as_uuid=True), sa.ForeignKey('sessions.id'), nullable=False, unique=True),
        sa.Column('recommendations', sa.JSON(), nullable=False),
        sa.Column('confidence', sa.String(), nullable=True),
        sa.Column('average_uncertainty', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False)
    )
    
    # Create indexes
    op.create_index('ix_sessions_user_id', 'sessions', ['user_id'])
    op.create_index('ix_responses_session_id', 'responses', ['session_id'])
    op.create_index('ix_responses_question_id', 'responses', ['question_id'])

def downgrade():
    op.drop_index('ix_responses_question_id', 'responses')
    op.drop_index('ix_responses_session_id', 'responses')
    op.drop_index('ix_sessions_user_id', 'sessions')
    op.drop_table('match_reports')
    op.drop_table('archetypes')
    op.drop_table('responses')
    op.drop_table('questions')
    op.drop_table('sessions')
    op.drop_table('users')

