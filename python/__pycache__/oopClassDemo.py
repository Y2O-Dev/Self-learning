o
    .B�d�  �                   @   s   G d d� d�Z e ddd�ZdS )c                   @   s>   e Zd Zdd� Zdd� Zedd� �Zejdd� �Zdd	� Zd
S )�Staffc                 C   s   || _ || _|| _td� d S )NzCreating Staff object)�	_position�name�pay�print)�self�	pPosition�pName�pPay� r
   �+/home/yakub/langHandson/pcc/oopClassDemo.py�__init__   s   zStaff.__init__c                 C   s   d| j � d| j� d| j� �S )NzPosition = z	, Name = z, Pay = )r   r   r   �r   r
   r
   r   �__str__   s   zStaff.__str__c                 C   s   t d� | jS )NzGetter Method)r   r   r   r
   r
   r   �position   s   zStaff.positionc                 C   s&   |dks|dkr|| _ d S td� d S )N�Manager�Basicz%Position is invalid. No changes made.)r   r   )r   �valuer
   r
   r   r      s   
c                 C   sD   d| j � d�}t|�}d| j � d�}t|�}t|�t|� | _| jS )Nz#
 Enter number of hour worked for %z: zEnter the hourly rate for )r   �input�intr   )r   �prompt�hours�
hourlyRater
   r
   r   �calculatePay   s   zStaff.calculatePayN)	�__name__�
__module__�__qualname__r   r   �propertyr   �setterr   r
   r
   r
   r   r      s    

r   r   �Seki�    N)r   �officeStaff1r
   r
   r
   r   �<module>   s    