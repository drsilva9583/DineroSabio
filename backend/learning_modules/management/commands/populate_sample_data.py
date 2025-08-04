from django.core.management.base import BaseCommand
from learning_modules.models import LearningModule, Lesson, Tip, Quiz, Example

class Command(BaseCommand):
    help = 'Populate the database with sample learning content for Dinero Sabio'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating sample data for Dinero Sabio...'))
        
        # Clear existing data
        LearningModule.objects.all().delete()
        
        # 1. How to Start Saving Module
        saving_module = LearningModule.objects.create(
            title="How to Start Saving",
            title_es="Cómo Empezar a Ahorrar",
            description="Learn simple, realistic saving strategies even on a low income",
            description_es="Aprende estrategias simples y realistas de ahorro incluso con bajos ingresos",
            category="saving",
            icon="💰",
            estimated_time=15,
            difficulty_level=1,
            order=1
        )
        
        # Emergency Fund Lesson
        emergency_lesson = Lesson.objects.create(
            module=saving_module,
            title="Emergency Fund Basics",
            title_es="Fundamentos del Fondo de Emergencia",
            content="An emergency fund is money set aside for unexpected expenses like car repairs or medical bills.",
            content_es="Un fondo de emergencia es dinero apartado para gastos inesperados como reparaciones del auto o facturas médicas.",
            lesson_type="content",
            order=1
        )
        
        Tip.objects.create(
            lesson=emergency_lesson,
            tip_text="Start with just $25 - even small amounts help!",
            tip_text_es="Comienza con solo $25 - ¡incluso las cantidades pequeñas ayudan!",
            is_highlighted=True
        )
        
        # 50/30/20 Rule Lesson
        budget_lesson = Lesson.objects.create(
            module=saving_module,
            title="The 50/30/20 Rule",
            title_es="La Regla 50/30/20",
            content="A simple budgeting method: 50% needs, 30% wants, 20% savings and debt.",
            content_es="Un método simple de presupuesto: 50% necesidades, 30% deseos, 20% ahorros y deudas.",
            lesson_type="calculator",
            order=2,
            calculator_config={
                "type": "budget_calculator",
                "inputs": ["monthly_income"],
                "outputs": ["needs_amount", "wants_amount", "savings_amount"]
            }
        )
        
        # 2. Money Myths Module
        myths_module = LearningModule.objects.create(
            title="Common Money Myths",
            title_es="Mitos Comunes del Dinero",
            description="Debunk harmful money myths common in our community",
            description_es="Desmiente mitos dañinos del dinero comunes en nuestra comunidad",
            category="myths",
            icon="💭",
            estimated_time=10,
            difficulty_level=1,
            order=2
        )
        
        # Stock Market Myth Lesson
        stock_myth_lesson = Lesson.objects.create(
            module=myths_module,
            title="Stock Market Myths",
            title_es="Mitos del Mercado de Valores",
            content="Let's bust some common myths about investing in stocks.",
            content_es="Vamos a desmentir algunos mitos comunes sobre invertir en acciones.",
            lesson_type="quiz",
            order=1
        )
        
        Quiz.objects.create(
            lesson=stock_myth_lesson,
            question="The stock market is only for rich people",
            question_es="La bolsa es sólo para ricos",
            is_myth=True,
            explanation="False! You can start investing with as little as $1 using apps like Acorns or Stash.",
            explanation_es="¡Falso! Puedes empezar a invertir con tan poco como $1 usando apps como Acorns o Stash."
        )
        
        Quiz.objects.create(
            lesson=stock_myth_lesson,
            question="You need thousands of dollars to start investing",
            question_es="Necesitas miles de dólares para empezar a invertir",
            is_myth=True,
            explanation="Myth! Many brokerages now allow fractional shares, so you can invest with any amount.",
            explanation_es="¡Mito! Muchas casas de bolsa ahora permiten acciones fraccionarias, así que puedes invertir con cualquier cantidad."
        )
        
        # 3. Cultural Investment Examples Module
        investment_module = LearningModule.objects.create(
            title="Investment Examples",
            title_es="Ejemplos de Inversión",
            description="Learn investing through familiar examples from our culture",
            description_es="Aprende a invertir a través de ejemplos familiares de nuestra cultura",
            category="investments",
            icon="🌮",
            estimated_time=20,
            difficulty_level=1,
            order=3
        )
        
        # Panadería Example Lesson
        panaderia_lesson = Lesson.objects.create(
            module=investment_module,
            title="Owning Part of a Panadería",
            title_es="Ser Dueño de Parte de una Panadería",
            content="Let's understand stocks by imagining you could own part of your favorite panadería.",
            content_es="Entendamos las acciones imaginando que puedes ser dueño de parte de tu panadería favorita.",
            lesson_type="story",
            order=1
        )
        
        Example.objects.create(
            lesson=panaderia_lesson,
            title="The Panadería Stock Example",
            title_es="El Ejemplo de Acciones de la Panadería",
            scenario="Imagine your local panadería wants to expand but needs money. They sell 'shares' to raise funds.",
            scenario_es="Imagina que tu panadería local quiere expandirse pero necesita dinero. Venden 'acciones' para recaudar fondos.",
            analogy="When you buy a stock, you're buying a tiny piece of a company, just like owning a small part of the panadería!",
            analogy_es="¡Cuando compras una acción, estás comprando un pedacito de una empresa, como ser dueño de una pequeña parte de la panadería!",
            image_description="Illustration of a panadería with multiple owners"
        )
        
        # 4. Financial Tips for Immigrants Module
        immigrants_module = LearningModule.objects.create(
            title="Financial Tips for Immigrants",
            title_es="Consejos Financieros para Inmigrantes",
            description="Practical financial advice for immigrants and first-generation families",
            description_es="Consejos financieros prácticos para inmigrantes y familias de primera generación",
            category="immigrants",
            icon="🌎",
            estimated_time=25,
            difficulty_level=2,
            order=4
        )
        
        # Banking Lesson
        banking_lesson = Lesson.objects.create(
            module=immigrants_module,
            title="Opening Your First Bank Account",
            title_es="Abriendo tu Primera Cuenta Bancaria",
            content="Learn how to open a bank account, even without traditional documentation.",
            content_es="Aprende cómo abrir una cuenta bancaria, incluso sin documentación tradicional.",
            lesson_type="content",
            order=1
        )
        
        Tip.objects.create(
            lesson=banking_lesson,
            tip_text="Many banks accept ITIN numbers instead of SSN",
            tip_text_es="Muchos bancos aceptan números ITIN en lugar de SSN",
            is_highlighted=True
        )
        
        Tip.objects.create(
            lesson=banking_lesson,
            tip_text="Credit unions are often more immigrant-friendly than big banks",
            tip_text_es="Las cooperativas de crédito suelen ser más amigables con inmigrantes que los bancos grandes"
        )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created sample data:\n'
                f'- {LearningModule.objects.count()} modules\n'
                f'- {Lesson.objects.count()} lessons\n'
                f'- {Tip.objects.count()} tips\n'
                f'- {Quiz.objects.count()} quizzes\n'
                f'- {Example.objects.count()} examples'
            )
        )