package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;

public class Myframe09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Myframe09 frame = new Myframe09();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Myframe09() {
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 287, 364);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(12, 10, 247, 34);
		contentPane.add(tf);
		tf.setColumns(10);
		JButton btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				/* clickNumber(e); */
				System.out.println(e.getButton());
				tf.setText(tf.getText()+btn1.getText());
			}
		});
		btn1.setBounds(12, 54, 53, 52);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(tf.getText()+btn2.getText());
			}
		});
		btn2.setBounds(108, 54, 53, 52);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(tf.getText()+btn3.getText());
			}
		});
		btn3.setBounds(206, 54, 53, 52);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(tf.getText()+btn4.getText());
			}
		});
		btn4.setBounds(12, 116, 53, 52);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(tf.getText()+btn5.getText());
			}
		});
		btn5.setBounds(108, 116, 53, 52);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(tf.getText()+btn6.getText());
			}
		});
		btn6.setBounds(206, 116, 53, 52);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(tf.getText()+btn7.getText());
			}
		});
		btn7.setBounds(12, 182, 53, 52);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(tf.getText()+btn8.getText());
			}
		});
		btn8.setBounds(108, 182, 53, 52);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(tf.getText()+btn9.getText());
			}
		});
		btn9.setBounds(206, 178, 53, 52);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(tf.getText()+btn0.getText());
			}
		});
		btn0.setBounds(12, 244, 53, 52);
		contentPane.add(btn0);
		
		JButton btnCall = new JButton("Call");
		btnCall.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JOptionPane.showMessageDialog(null, tf.getText(), "Calling", JOptionPane.INFORMATION_MESSAGE);
			}
		});
		btnCall.setBounds(108, 244, 151, 52);
		contentPane.add(btnCall);
	}
	
	public void myAlert(MouseEvent e) {
		JOptionPane.showMessageDialog(null, e + "calling");
	}
	
	public void clickNumber(MouseEvent e) {
		String old = tf.getText();
		JButton temp = (JButton) e.getSource();
		String num = temp.getText();
//		System.out.println(num);
		tf.setText(old + num);
	}

}
