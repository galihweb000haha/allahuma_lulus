"""pembaruan 2

Revision ID: a0462e2f9822
Revises: 
Create Date: 2023-02-20 14:56:43.416284

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a0462e2f9822'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gender', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('no_hp', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('foto', sa.Text(), nullable=True))

    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.alter_column('nim',
               existing_type=mysql.CHAR(length=8),
               type_=sa.String(length=8),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=52),
               type_=sa.String(length=50),
               nullable=True)
        batch_op.alter_column('state',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=20),
               nullable=True)
        batch_op.alter_column('gender',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
        batch_op.alter_column('batch_year',
               existing_type=mysql.YEAR(),
               type_=sa.DateTime(),
               nullable=True)
        batch_op.alter_column('gpa_score',
               existing_type=mysql.FLOAT(),
               nullable=True)
        batch_op.alter_column('toefl_score',
               existing_type=mysql.FLOAT(),
               nullable=True)
        batch_op.alter_column('parents_income',
               existing_type=mysql.DOUBLE(asdecimal=True),
               type_=sa.Float(),
               nullable=True)
        batch_op.alter_column('address',
               existing_type=mysql.TEXT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=mysql.TEXT(),
               nullable=False)
        batch_op.alter_column('parents_income',
               existing_type=sa.Float(),
               type_=mysql.DOUBLE(asdecimal=True),
               nullable=False)
        batch_op.alter_column('toefl_score',
               existing_type=mysql.FLOAT(),
               nullable=False)
        batch_op.alter_column('gpa_score',
               existing_type=mysql.FLOAT(),
               nullable=False)
        batch_op.alter_column('batch_year',
               existing_type=sa.DateTime(),
               type_=mysql.YEAR(),
               nullable=False)
        batch_op.alter_column('gender',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
        batch_op.alter_column('state',
               existing_type=sa.String(length=20),
               type_=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=52),
               nullable=False)
        batch_op.alter_column('nim',
               existing_type=sa.String(length=8),
               type_=mysql.CHAR(length=8),
               nullable=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('foto')
        batch_op.drop_column('no_hp')
        batch_op.drop_column('gender')

    # ### end Alembic commands ###
