from django.db import models

# Create your models here.
class Receita(models.Model):
    # --- Campos do Modelo ---
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    
    # Campo para imagens das receitas
    # Lembre-se de instalar a biblioteca Pillow: pip install Pillow
    image = models.ImageField(upload_to='receitas/images/', blank=True, null=True)
    
    # Campos de data e hora automáticos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # --- Métodos do Modelo ---
    def __str__(self):
        """
        Retorna a representação em string do objeto, que neste caso é o título.
        Isso é o que aparecerá no painel de administração do Django.
        """
        return self.title

    # --- Metadados do Modelo ---
    class Meta:
        """
        Configurações adicionais para o modelo.
        """
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering = ['-created_at']  # Ordena as receitas da mais nova para a mais antiga