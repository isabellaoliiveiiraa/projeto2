from django.db import models

class Receita(models.Model):
    # 1. A lista de categorias foi movida para fora da classe antiga e o nome corrigido
    CATEGORIAS = [
        ('comida', 'Comida'),
        ('sobremesa', 'Sobremesa'),
        ('drinks', 'Drinks'),
    ]

    title = models.CharField("Titulo", max_length=200)
    description = models.TextField("Descrição")
    ingredients = models.TextField("Ingredientes")
    instructions = models.TextField("Instruções")
    
    image = models.ImageField("imagem", upload_to='receitas/images/', blank=True, null=True)

    # 2. O 'choices' agora usa a variável correta 'CATEGORIAS'
    categoria = models.CharField("Categoria", max_length=50, choices=CATEGORIAS, default='comida')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering = ['-created_at']